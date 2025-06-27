#!/bin/bash

# Config vars
RESOURCE_GROUP="networksecurity-rg"
STORAGE_ACCOUNT="netwworksecurity"
CONTAINER_NAME="networksecuritycontainer"
LOCATION="westeurope"

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create storage account
az storage account create \
  --name $STORAGE_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS

# Create blob container
az storage container create \
  --account-name $STORAGE_ACCOUNT \
  --name $CONTAINER_NAME \
  --public-access off

# Generate SAS token valid for 24h (adjust expiry as needed)
SAS_TOKEN=$(az storage container generate-sas \
  --account-name $STORAGE_ACCOUNT \
  --name $CONTAINER_NAME \
  --permissions rwlc \
  --expiry $(date -u -d "+1 day" '+%Y-%m-%dT%H:%MZ') \
  --output tsv)

# Print container URL with SAS token
echo "Container URL:"
echo "https://${STORAGE_ACCOUNT}.blob.core.windows.net/${CONTAINER_NAME}?${SAS_TOKEN}"
