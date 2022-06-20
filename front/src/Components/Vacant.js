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
                    Координатор волонтёров
                </h1>
                <h2>
                    Задачи:
                </h2>
                <ul class="">
                    
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
                    <button type="submit" class="btn-main-page">
                        ПОДРОБНЕЕ
                    </button>
                </form>
            </div>
        </main>
        );
    }
}

export default Vacant;