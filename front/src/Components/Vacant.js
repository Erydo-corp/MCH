import React, {Component} from "react";
import li from "./assets/li.svg";
import callout from "./assets/Callout.svg";
import back from "./assets/back.svg";

class Vacant extends Component{
    render(){
        return(
            <main>
            <div class="main_image">
                <img src={callout} alt=""/>
            </div>
            <div class="main-ul">
                <h1>
                    {this.props.title}
                </h1>
                <h2>
                    Задачи:
                </h2>
                <ul class="">
                    <li>
                        <img src={li}/>
                        <p>{this.props.discrip_one}</p>
                    </li>
                    <li>
                        <img src={li}/>
                        <p>
                          {this.props.discrip_two}  
                        </p>
                        </li>
                    <li>
                        <img src={li}/>
                        <p>
                            {this.props.discrip_three}
                        </p>
                    </li>
                </ul>
                <a href="vacansi">
                <button class="btn-main-page">
                        ПОДРОБНЕЕ
                    </button>
                </a>
            </div>
        </main>
        );
    }
}

export default Vacant;