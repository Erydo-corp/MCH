import React, {Component} from "react";
import Vacant from "./Vacant";

class MainPage extends Component {
    

    render(){
        return(
            <div>
                <h2 class="main-h2">Вакансии</h2>
                <Vacant />
            </div>
        );
    }
}

export default MainPage;