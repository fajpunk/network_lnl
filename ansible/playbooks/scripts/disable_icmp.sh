iptables -A INPUT -p icmp -j DROP
iptables-save > /etc/iptables/rules.v4
