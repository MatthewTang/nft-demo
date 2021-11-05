/* eslint-disable spaced-comment */
/// <reference types="react-scripts" />
import { MintNFT } from "./mintNFT"
import eth from '../img/eth.png'
import dai from '../img/dai.png'
import luckin from '../img/luckin.png'

export type Collectible = {
    id: string
    image: string
    name: string
}

const collectibles: Array<Collectible> = [
    //{
    //    id: "0",
    //    image: eth,
    //    name: "ETH"
    //},
    //{
    //    id: "1",
    //    image: dai,
    //    name: "DAI"
    //},
    {
        id: "2",
        image: luckin,
        name: "LUCKIN"
    }
]

export const Main = () => {
    return (
        <div>
            Main
            <MintNFT collectibles={collectibles} />
        </div>
    )

}