import { Collectible } from "../Main"
import { MintForm } from "./MintForm"

interface CollectiblesProps {
    collectibles: Array<Collectible>
}

export const Collectibles = ({ collectibles }: CollectiblesProps) => {
    return (
        <div>
            <h1>Collectibles</h1>
            {
                collectibles.map((collectible: Collectible, index) => {
                    return <MintForm collectible={collectible} key={index} />
                })
            }

        </div>
    )
}