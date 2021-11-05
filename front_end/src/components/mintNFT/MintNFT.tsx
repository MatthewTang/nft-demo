import { Button } from "@material-ui/core"
import { useTokenCounter } from "../../hooks/useTokenCounter"
import { Collectible } from "../Main"
import { Collectibles } from "./Collectibles"

interface MintNFTProps {
    collectibles: Array<Collectible>
}



export const MintNFT = ({ collectibles }: MintNFTProps) => {
    const tokenCounter = useTokenCounter();

    // console.log(tokenCounter)

    return (
        <>
            <p>{tokenCounter && tokenCounter.toString()}</p>

            <Collectibles collectibles={collectibles} />
        </>
    )

}