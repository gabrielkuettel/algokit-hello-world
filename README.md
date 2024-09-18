# algokit-hello-world

This project implements a simple Algorand smart contract using AlgoKit. It consists of two main parts:

1. Contract ([contract.py](./projects/algokit-hello-world/smart_contracts/hello_world/contract.py)): This defines a `HelloWorld` contract with a `hello` method that takes a `name`, creates a greeting, stores it to the application's box storage, and returns it.

2. Deployment ([deploy_config.py](./projects/algokit-hello-world/smart_contracts/hello_world/deploy_config.py)): This deploys the contract and calls the `hello` method with a hardcoded name.


**App Call Transaction ID:**
[SFYRE5YWGRCCVEQDUPMAL7DUTFUC7G22PJNDN2HLE5LZ4HBRHSVA](https://lora.algokit.io/testnet/transaction/SFYRE5YWGRCCVEQDUPMAL7DUTFUC7G22PJNDN2HLE5LZ4HBRHSVA)

**App ID:**
[722260727](https://lora.algokit.io/testnet/application/722260727)
