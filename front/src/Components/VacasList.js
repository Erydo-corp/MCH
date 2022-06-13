import React, {Component} from "react";
import OneVac from "./OneVac"

class VacansList extends Component{
    render(){
        return(
            <main class="main-vacant-list">
                <div class="header">
                    <h1>Вакансии</h1>
                    <h2>Сферы деятельности:</h2>
                    <div class="field-activity"><p>#социальный;</p> <p>#административный;</p> <p>#медицина;</p>
                        <p>#культура;</p><p>#медиа</p></div>
                    <div class="filter">
                        <h2>Изменить фильтр сфер</h2>
                        <img src="/asset/Vector.svg" alt=""/>
                    </div>
                </div>
                <OneVac/>
            </main>
        );
    }
}
export default VacansList;