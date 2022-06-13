import React, {Component} from "react";
import art from "./assets/Art.svg";
import garage from "./assets/garage.svg";
import gsci from "./assets/gsci.svg";
import treti from "./assets/treti.svg";
import vinza from "./assets/vinzavod.svg";

class Footer extends Component{
    render(){
        return (
            <footer>
                <img src={treti} alt=""/>
                <img src={garage} alt=""/>
                <img src={art} alt=""/>
                <img src={gsci} alt=""/>
                <img src={vinza} alt=""/>
            </footer>
        );
    }
}

export default Footer;