from scripts.advanced.create_metadata import upload_to_ipfs
import pytest


def test_upload_to_ipfs():
    # ensure local ipfs daemon is running and comment out the following line
    pytest.skip()
    # arrange
    file_path = "./img/pug.png"
    # act
    img_url = upload_to_ipfs(file_path)
    # assert
    assert (
        img_url
        == "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png"
    )
