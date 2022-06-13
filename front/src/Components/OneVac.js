import React, {Component} from "react";

class OneVac extends Component{
    render(){
        return(
            <div class="vacant-list">
            <div>
                <h1>Волонтёр по посещению людей</h1>
                <h2>Задачи:</h2>
                <ul>
                    <li>
                        <img src="/asset/li.svg"/>
                        <p>Курировать деятельности волонтерского движения Фонда</p>
                    </li>
                    <li>
                        <img src="/asset/li.svg"/>
                        <p>Проводение культурно-массовых мероприятия и организация свободного времени пожилых людей</p>
                    </li>
                    <li>
                        <img src="/asset/li.svg"/>
                        <p>Помощь в уходе за пожилыми людьми</p>
                    </li>
                </ul>
                <img class="imgList" src="/asset/Bags.svg" alt=""/>
                <button class="otc">
                    ОТКЛИКНУТЬСЯ
                </button>
                <button class="btn-main-page">
                    Показать контакты
                </button>
            </div>
        </div>
        );
    }
}
export default OneVac;