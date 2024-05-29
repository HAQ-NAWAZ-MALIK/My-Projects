
#include <stdio.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <net/ethernet.h>

void process_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet) {
    struct ether_header *eth_header;
    struct ip *ip_header;
    struct tcphdr *tcp_header;

    int size_ip;
    int size_tcp;

    // Ethernet header
    eth_header = (struct ether_header *)packet;
    printf("Ethernet: %.6s -> %.6s\n", eth_header->ether_shost, eth_header->ether_dhost);

    // IP header
    size_ip = sizeof(struct ether_header);
    ip_header = (struct ip *)(packet + size_ip);
    printf("IP: %s -> %s\n", inet_ntoa(ip_header->ip_src), inet_ntoa(ip_header->ip_dst));

    // TCP header
    size_tcp = size_ip + (ip_header->ip_hl * 4);
    tcp_header = (struct tcphdr *)(packet + size_tcp);
    printf("TCP: %d -> %d\n", ntohs(tcp_header->th_sport), ntohs(tcp_header->th_dport));

    printf("\n");
}

int main() {
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];
    struct bpf_program fp;
    char filter_exp[] = "ip proto tcp";
    bpf_u_int32 net;

    // Open the network interface for packet capturing
    handle = pcap_open_live("en0", BUFSIZ, 1, 1000, errbuf);
    if (handle == NULL) {
        fprintf(stderr, "Could not open device: %s\n", errbuf);
        return 1;
    }

    // Set the BPF filter for capturing TCP packets
    if (pcap_compile(handle, &fp, filter_exp, 0, net) == -1) {
        fprintf(stderr, "Could not parse filter %s: %s\n", filter_exp, pcap_geterr(handle));
        return 2;
    }
    if (pcap_setfilter(handle, &fp) == -1) {
        fprintf(stderr, "Could not install filter %s: %s\n", filter_exp, pcap_geterr(handle));
        return 3;
    }

    // Start capturing packets
    printf("Capturing packets...\n");
    pcap_loop(handle, -1, process_packet, NULL);

    pcap_freecode(&fp);
    pcap_close(handle);

    return 0;
}