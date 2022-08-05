# Apeworx test

## ApeWorx installation

```sh
pipx install eth-ape infura alchemy vyper foundry
```

## Foundry installation

```sh
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

## Test

```sh
ape test
```

## Test on mainnet-fork

```sh
ape test --network :mainnet-fork:foundry
```

## Deploy on mainnet

```sh
ape run deploy --network :mainnet:infura
```