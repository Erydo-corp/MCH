import React, {Component} from "react";


class Advertisement extends Component{
    render(){
        return(
            <div class="advertisement">
    <h1>Координатор волонтёров</h1>
    <h2>Благотворитиельный Фонд “ЗА Жизнь”</h2>
    <h3>Москва, Озерковская набережная, 22/4-11А</h3>
    <p>Требуемый опыт: #социальный; #административный; #культура </p>
    <p>Возраст: 20-35 лет</p>
    <p>Частичная занятость,  гибкий график</p>
    <div class="discription-advent">
        <h3>Задачи:</h3>
        <ul>
            <li>
                <img src="/asset/li.svg"/>
                <p>Курировать деятельности волонтерского движения Фонда</p>
            </li>
            <li>
                <img src="/asset/li.svg"/>
                <p>Организовывать и проводить культурно-массовые мероприятия 
                    с участием волонтеров</p>
            </li>
            <li>
                <img src="/asset/li.svg"/>
                <p>Разрабатывать и внедрять системы мотивации и поощрения для волонтеров</p>
            </li>
            <li>
                <img src="/asset/li.svg"/>
                <p>формировать информационную повестку для волонтерского движения</p>
            </li>
        </ul>
        <h3>Бонусы:</h3>
        <ul>
            <li>
                <img src="/asset/Ellipse.svg"/>
                <p>Офис в центре Москвы: м. Третьяковская</p>
            </li>
            <li>
                <img src="/asset/Ellipse.svg"/>
                <p>сертификаты на посещение ГЦСИ</p>
            </li>
            <li>
                <img src="/asset/Ellipse.svg"/>
                <p>возможность дальнейшего официального трудоустройства</p>
            </li>
        </ul>
    </div>
    <h3>Ключевые навыки:</h3>
    <div class="keys">
        <button>Работа в команде</button>
        <button>Многозадачность</button>
        <button>Органнизованность</button>
        <button>Коммуникабельность</button>
    </div>
    <button class="otc">
        ОТКЛИКНУТЬСЯ
    </button>
    <img src="/asset/Callout.svg" alt="" class="img-adv"/>
    <div class="times">
        <h3>Срочно</h3>
        <h3>В течении недели</h3>
        <h3>В течении месяца</h3>
    </div>
    </div>
        );
    }
}

export default Advertisement