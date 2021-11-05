import { Button, CircularProgress, Snackbar } from "@material-ui/core"
import { useEffect, useState } from "react";
import { useCreateCollectible } from "../../hooks/useCreateCollectible";
import { Collectible } from "../Main"
import { useNotifications } from "@usedapp/core";
import { makeStyles } from "@material-ui/core";
import { Alert } from "@material-ui/lab";
import { constants, utils } from 'ethers'
import { useContractFunction, useEthers } from '@usedapp/core'
import networkMapping from '../../chain-info/deployments/map.json'
import { useTokenCounter } from "../../hooks/useTokenCounter";

const useStyles = makeStyles(theme => ({
    container: {
        padding: theme.spacing(4),
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        gap: theme.spacing(1),
    },
    tokenImg: {
        width: "32px"
    },
}))

const sample_token_uri = "https://ipfs.io/ipfs/QmWJDScS8uUvL4C93LBLsbJv2zXv9numnCRmRS615yfGGk?filename=luckin.json"
const OPENSEA_URL = "https://testnets.opensea.io/assets/"  // {} = asset_contract_address, {} = token_id

interface CollectibleProps {
    collectible: Collectible
}

export const MintForm = ({ collectible }: CollectibleProps) => {
    const classes = useStyles();
    const { image, name, id } = collectible;


    const { chainId } = useEthers()
    const simpleCollectibleAddress = chainId ? networkMapping[String(chainId)]['SimpleCollectible'][0] : constants.AddressZero

    const tokenCounter = useTokenCounter();

    const { createCollectible, createCollectibleState: createCollectibleState } = useCreateCollectible()
    const { notifications } = useNotifications()

    const handleClick = () => {
        return createCollectible(sample_token_uri)
    }

    const handleCloseSnack = () => {
        setShowCreateCollectibleSuccess(false)
    }

    const isMining = createCollectibleState.status === 'Mining'
    const [showCreateCollectibleSuccess, setShowCreateCollectibleSuccess] = useState(false);

    useEffect(() => {
        if (notifications.filter(notification => notification.type === 'transactionSucceed' &&
            notification.transactionName === "create Collectible").length > 0) {
            console.log("minted")
            setShowCreateCollectibleSuccess(true)
        }
    }, [notifications, createCollectibleState, showCreateCollectibleSuccess])


    return (
        <div className={classes.container}>
            <div> {name}</div>
            <img className={classes.tokenImg} src={image} alt={name} />
            <div>
                <Button
                    onClick={handleClick}
                    variant="contained"
                >
                    {isMining ? <CircularProgress size={26} /> : "Mint"}
                </Button>
            </div>
            <Snackbar
                open={showCreateCollectibleSuccess}
                autoHideDuration={6000}
                onClose={handleCloseSnack}
            >
                <Alert>
                    {name} minted successfully! Check your {name} at OpenSea's testnet {`${OPENSEA_URL}/${simpleCollectibleAddress}/${tokenCounter && tokenCounter.toNumber() - 1}`}
                </Alert>
            </Snackbar>
        </div>
    )
}