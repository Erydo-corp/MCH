import React, {Component} from "react";
import li from "./assets/li.svg";
import callout from "./assets/Callout.svg";
import liOrange from "./assets/li-orange.svg";
import "../style/OneVac.css"
class OneVac extends Component{
    constructor(props){
        super(props)
        this.state = {
            vacant: {
                    name: "",
                    task: [],
                    requirements: [],

            },
        }
       
        this.loadVacant = this.loadVacant.bind(this)
    }
    loadVacant(){
        fetch('http://127.0.0.1:8000/api/partner/vacancys/2/', {
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
        this.setState({vacant: commits
        });
    });
    }

    componentDidMount(){
        this.loadVacant()
    }



    render(){
        for( let i = 0; this.state.vacant.id>=0; i++){
            let requirement = this.state.vacant.requirements;
            let task = this.state.vacant.task;
            let bonus = this.state.vacant.bonus;
        return(
            <div class="discriptions-vacants">
            <div class="discription-vacant">
                <h1>{this.state.vacant.name}</h1>
                <h2>{this.state.vacant.sphere}</h2>
                <h3>{this.state.vacant.location}</h3>
                <p>Требуемый опыт: {requirement.map((item)=>
                    <b key={item.id}>{"#"+item + " "} </b>
                )}</p>
                {/*
                <p>Возраст:</p>
       
                <p>Частичная занятость,  гибкий график</p>
                 */}
                <h2>Задачи:</h2>
                <ul class="vacant-ul">
                    {task.map((item)=>
                     <li key={item.id}>
                        <img src={li} alt="li"/>
                        <p>{item}</p>
                    </li>
                    )}
                </ul>
                <h2 class="bon">Бонусы:</h2>
                <ul class="vacant-ul">
                    { bonus.map((item)=>
                    <li  key={item.id}>
                        <img src={liOrange} alt="li-orange"/>
                        <p>{item}</p>
                    </li>
                    )}
                </ul>
            </div>
            <div class="lost">
                <h2>Срочно</h2>
                <h2>В течении недели</h2>
                <h2>В течении месяца</h2>
                <img src={callout} alt=""/>
            </div>
            {console.log(i)}
        </div>
        );
    }
}
}
export default OneVac;