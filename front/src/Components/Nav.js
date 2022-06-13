import React, {Component} from "react";
import Btn from "./Btn";
import logo from "./assets/logo.svg";

class Nav extends Component{
// Не забыть в кнопки проставить урл hre
    render(){
        return(
        <nav>
            <img src={logo} alt="лого" width="200px"/>
            <Btn name="item one" hre='register'>Волонтёр</Btn>
            <Btn name="item two">Партнёр</Btn>
            <Btn name="item three">Магазин</Btn>
            <Btn name="item four">ЛК</Btn>
        </nav>
        );
    };
}


export default Nav