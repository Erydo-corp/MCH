import React, {Component} from "react";

class Btn extends Component{

    render(){
        let name = this.props.name;
        return(
            <button className={name}>
                <a href={this.props.hre}>
                    {this.props.children}
                </a>
            </button>
        );
    };
}

export default Btn;