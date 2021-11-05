
import { useContractFunction, useEthers } from '@usedapp/core'
import { constants, utils } from 'ethers'
import SimpleCollectible from '../chain-info/contracts/SimpleCollectible.json'
import networkMapping from '../chain-info/deployments/map.json'
import { Contract } from '@ethersproject/contracts';


export const useCreateCollectible = () => {
    // approve

    const { chainId } = useEthers()
    const { abi } = SimpleCollectible

    const simpleCollectibleAddress = chainId ? networkMapping[String(chainId)]['SimpleCollectible'][0] : constants.AddressZero
    const simpleCollectibleInterface = new utils.Interface(abi)
    const simpleCollectibleContract = new Contract(simpleCollectibleAddress, simpleCollectibleInterface)

    const { send: createCollectible, state: createCollectibleState } =
        useContractFunction(
            simpleCollectibleContract, "createCollectible", {
            transactionName: "create Collectible"
        }
        )


    return { createCollectible, createCollectibleState }
}