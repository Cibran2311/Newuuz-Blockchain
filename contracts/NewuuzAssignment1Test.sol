// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import {IERC721} from "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import {IERC721Receiver} from "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";

/// @notice Course-controlled NFT used for the professor receive/return flow.
contract NewuuzProfessorNFT is ERC721, Ownable {
    uint256 private _nextTokenId = 1;

    constructor() ERC721("NewUUZ Professor NFT", "NUPROF") Ownable(msg.sender) {}

    function mintTo(address student) external onlyOwner returns (uint256 tokenId) {
        require(student != address(0), "student is zero address");
        tokenId = _nextTokenId++;
        _safeMint(student, tokenId);
    }
}

/// @notice Student NFT with a public mint function for the Assignment 1 test.
contract NewuuzStudentNFT is ERC721 {
    uint256 private _nextTokenId = 1;

    constructor() ERC721("NewUUZ Student NFT", "NUSTUDENT") {}

    function mint() external returns (uint256 tokenId) {
        tokenId = _nextTokenId++;
        _safeMint(msg.sender, tokenId);
    }
}

/// @notice ERC721 receiver used as the configured special contract.
contract NewuuzSpecialNFTReceiver is IERC721Receiver, Ownable {
    event NFTReceived(
        address indexed nftContract,
        address indexed operator,
        address indexed from,
        uint256 tokenId
    );

    constructor() Ownable(msg.sender) {}

    function onERC721Received(
        address operator,
        address from,
        uint256 tokenId,
        bytes calldata
    ) external returns (bytes4) {
        emit NFTReceived(msg.sender, operator, from, tokenId);
        return IERC721Receiver.onERC721Received.selector;
    }

    function returnNFT(
        address nftContract,
        uint256 tokenId,
        address recipient
    ) external onlyOwner {
        require(recipient != address(0), "recipient is zero address");
        IERC721(nftContract).safeTransferFrom(address(this), recipient, tokenId);
    }
}
