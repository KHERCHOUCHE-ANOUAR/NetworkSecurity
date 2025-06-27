# Variables
RESOURCE_GROUP="networksecurity-rg"
VM_NAME="networksecurity-vm"
LOCATION="westeurope"
IMAGE="Ubuntu2204"
ADMIN_USER="anouar"
SSH_KEY="$HOME/.ssh/id_rsa.pub"

# Create VM
az vm create \
  --resource-group $RESOURCE_GROUP \
  --name $VM_NAME \
  --image $IMAGE \
  --admin-username $ADMIN_USER \
  --ssh-key-values $SSH_KEY \
  --size Standard_B2s \
  --public-ip-address-dns-name "networksecurity-vm-dns"

# Open Docker port if needed (e.g. for HTTP services)
az vm open-port --resource-group $RESOURCE_GROUP --name $VM_NAME --port 8080

# Done — get VM public IP
az vm list-ip-addresses --resource-group $RESOURCE_GROUP --name $VM_NAME --output table
