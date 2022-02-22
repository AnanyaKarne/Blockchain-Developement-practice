// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage{

    //this will initialized to 0!
    uint256 favoriteNumber;
    bool favoriteBool;

    struct People{
        uint256 favoriteNumber;
        string name;

    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;


    People public person=People(2,"Patrick");

    function store(uint256 _favoriteNumber) public{
        favoriteNumber=_favoriteNumber;
    }

    //view, pure->will do math, but not save state
    function retrieve() public view returns(uint256){
        return favoriteNumber+favoriteNumber;
    }

    function add(string memory _name,uint256 _favoriteNumber) public{
        people.push(People(_favoriteNumber,_name));
        nameToFavoriteNumber[_name]=_favoriteNumber;
    }

}
