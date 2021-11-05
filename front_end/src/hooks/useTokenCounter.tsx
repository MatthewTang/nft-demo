
import { useContractFunction, useEthers, ContractCall, useContractCall } from '@usedapp/core'
import { constants, utils } from 'ethers'
import SimpleCollectible from '../chain-info/contracts/SimpleCollectible.json'
import networkMapping from '../chain-info/deployments/map.json'
import { Contract } from '@ethersproject/contracts';


export const useTokenCounter = () => {
    // approve

    const { chainId } = useEthers()
    const { abi } = SimpleCollectible


    const simpleCollectibleAddress = chainId ? networkMapping[String(chainId)]['SimpleCollectible'][0] : constants.AddressZero
    const simpleCollectibleInterface = new utils.Interface(abi)
    const contract_call = {
        abi: simpleCollectibleInterface,
        address: simpleCollectibleAddress,
        method: "tokenCounter",
        args: []
    }


    const [token] = useContractCall(contract_call) ?? []
    return token
}

