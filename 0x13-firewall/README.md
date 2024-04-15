# 0x13. Firewall
> A firewall is a network security system that monitors and controls
incoming and outgoing network traffic based on predetermined security rules

* Types of firewall
1. packet filter
2. connection tracking
3. application layer
4. endpoint specific

## Tasks
0. Block all incoming traffic but
> 22 (SSH)
> 443 (HTTPS SSL)
> 80 (HTTP)

1. Port forwarding
> Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP
