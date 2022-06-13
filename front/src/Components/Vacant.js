import React, {Component} from "react";
import li from "./assets/li.svg";
import callout from "./assets/Callout.svg";
import back from "./assets/back.svg";

class Vacant extends Component{
    render(){
        return(
        <div className="vacantsi">
            <img src={callout} alt=""/>
            <div className="discription">
                <h1>
                    Координатор волонтёров
                </h1>
                <h2>
                    Задачи:
                </h2>
                <ul>
                    <li>
                        <img src={li}/>
                        <p>Курировать деятельности волонтерского движения Фонда</p>
                    </li>
                    <li>
                        <img src={li}/>
                        <p>
                            Организовывать и проводить культурно-массовые мероприятия 
                        с участием волонтеров
                        </p>
                        </li>
                    <li>
                        <img src={li}/>
                        <p>
                            Разрабатывать и внедрять системы мотивации и поощрения для волонтеров
                        </p>
                    </li>
                </ul>
                <form action="" method="get">
                    <button type="submit" className="btn-main-page">
                        ПОДРОБНЕЕ
                    </button>
                </form>
            </div>
            <img className="back" src={back} alt=""/>
        </div>
        );
    }
}

export default Vacant;