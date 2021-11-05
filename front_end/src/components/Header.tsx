import { useEthers } from "@usedapp/core"
import { Button, makeStyles } from "@material-ui/core"

const useStyles = makeStyles(theme => ({
    container: {
        padding: theme.spacing(4),
        display: "flex",
        justifyContent: "flex-end",
        gap: theme.spacing(1),
    }
}))

export const Header = () => {

    const { account, activateBrowserWallet, deactivate } = useEthers()
    const classes = useStyles();

    const isConnected = account !== undefined

    return (
        <div className={classes.container}>
            <Button
                color="primary"
                variant="contained"
                onClick={() => {
                    if (account) {
                        deactivate()
                    } else {
                        activateBrowserWallet()
                    }
                }}
            >
                {isConnected ? "Disconnect" : "Connect"}
            </Button>
        </div>
    )


}