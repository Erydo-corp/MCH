import React, {Component} from "react";
import Vacant from "./Vacant";

class MainPage extends Component {
    constructor(props){
        super(props)
        this.state = {
            title: "Координатор волонтёров",
            discrip_one: "Курировать деятельности волонтерского движения Фонда",
            discrip_two: "Организовывать и проводить культурно-массовые мероприятия с участием волонтеров",
            discrip_three: "Разрабатывать и внедрять системы мотивации и поощрения для волонтеров"
        }
        this.setState = {
            title: ""
        }
    }
    
    render(){
        return(
            <div>
                <h2 class="main-h2">Вакансии</h2>
                <Vacant 
                title={this.state.title}
                discrip_one={this.state.discrip_one}
                discrip_two={this.state.discrip_two}
                discrip_three={this.state.discrip_three}/>

            </div>
        );
    }
}

export default MainPage;