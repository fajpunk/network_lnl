iptables -A INPUT -p udp -j DROP
iptables-save > /etc/iptables/rules.v4
