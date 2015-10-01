Notes
=====

* ping
  * ping a working server
  * ping a non-working server
  * ssh into a non-working server
  * How can it not ping???
  * explain works over ICMP
* netcat
  * Listen for messages on localhost
  * Send messages on localhost
  * Listen for messages in one container, send in another
  * Listen for messages on host, send in container, vice versa
  * Verify connections
  * Demonstrate testing whether or not there's a TCP service running on port ...
  * Mention that UDP connection stuff is very weird
* tcpdump
 * See all the traffic to a host
 * filter traffic
 * Can be used to confirm that traffic is getting to where the service lives (a problem with the service, not the network)
 * Pretend netcat -l is our service in one container
 * Verify with tcpdump
 * Stop it in the one container, verify that tcpdump still shows traffic.
 * Need root access
* traceroute
  * show how it doesn't work if UDP is blocked
  * show how it works with TCP
