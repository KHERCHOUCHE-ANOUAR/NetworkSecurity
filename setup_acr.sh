RESOURCE_GROUP="networksecurity-rg"
ACR_NAME="networksecurityacr"
LOCATION="westeurope"


# Create Azure Container Registry
az acr create --resource-group $RESOURCE_GROUP --name $ACR_NAME --sku Basic --location $LOCATION

# Show ACR login server
az acr show --name $ACR_NAME --query "loginServer" --output tsv
