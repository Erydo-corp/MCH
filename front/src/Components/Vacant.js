import React, {Component} from "react";
import li from "./assets/li.svg";
import callout from "./assets/Callout.svg";
import back from "./assets/back.svg";

class Vacant extends Component{
    constructor(props){
        super(props)
        this.state = {
            vacant: {
                    name: "",
                    task: []
            }
        }
       
        this.loadVacant = this.loadVacant.bind(this)
    }
    loadVacant(){
        fetch('http://127.0.0.1:8000/api/partner/vacancys/1/', {
        method: "GET",
        //mode: "no-cors",
    })
    .then(response => {
        if(response.ok){
            return response.json();
        }else {
            console.log("нет")
        }
    })
    .then(commits => {
        this.setState({vacant: commits});
    });
    }

    componentDidMount(){
        this.loadVacant()
    }

    render(){
        return(
            <main>
            <div class="main_image">
                <img src={callout} alt=""/>
            </div>
            <div class="main-ul">
                <h1>
                    {this.state.vacant.name}
                </h1>
                <h2>
                    Задачи:
                </h2>
                <ul class="">
                    <li>
                        <img src={li} alt='li'/>
                        <p>{this.state.vacant.task[0]}</p>
                    </li>
                    <li>
                        <img src={li} alt='li'/>
                        <p>
                          {this.state.vacant.task[1]}  
                        </p>
                        </li>
                    <li>
                        <img src={li} alt='li'/>
                        <p>
                            {this.state.vacant.task[2]}
                        </p>
                    </li>
                </ul>
                <a href="diskription-vacansy">
                <button class="btn-main-page">
                        ПОДРОБНЕЕ
                    </button>
                </a>
            </div>
            <div class="main-back">
                 <img src={back} alt=""/>
            </div>
        </main>
        );
    }
}

export default Vacant;