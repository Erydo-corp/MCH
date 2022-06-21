import React, {Component} from "react";
import logo from "./assets/logo.svg";
import user from "./assets/user.svg"

class Nav extends Component{
    render(){
        return(
            <nav>
        <div class="nav-logo">
            <img src={logo} alt=""/>
        </div>
        <div class="btn-nav">
            <a href="/register"><button class="one">Волонтер</button></a>
            <a href=""><button class="two">Партнёр</button></a>
            <a href=""><button class="three">Магазин</button></a>
            <a href="" class="user"><img src={user} alt=""/></a>
        </div>
    </nav>
        );
    };
}


export default Nav