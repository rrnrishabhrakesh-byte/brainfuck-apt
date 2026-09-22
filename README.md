# Install brainfuck-interpreter-apt

### bash
curl -fsSL https://rrnrishabhrakesh-byte.github.io/brainfuck-apt/public.key \
  | sudo gpg --dearmor --yes -o /etc/apt/keyrings/bf-archive-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/bf-archive-keyring.gpg] https://rrnrishabhrakesh-byte.github.io/brainfuck-apt stable main" \
  | sudo tee /etc/apt/sources.list.d/bf.list > /dev/null

sudo apt update
sudo apt install bf

# Remove brainfuck-interpreter-apt

### bash
sudo apt remove --purge bf
sudo rm -f /etc/apt/sources.list.d/bf.list
sudo rm -f /etc/apt/keyrings/bf-archive-keyring.gpg
sudo rm -f /var/cache/apt/archives/bf_*.deb
sudo apt update
### Check it has been removed:
command -v bf
apt-cache policy bf
