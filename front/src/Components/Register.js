import React, {Component} from "react";

class Register extends Component{
    constructor(props){
        super(props)
        this.state = {
            name: '',
            age: '',
            email: '',
            tel: ''
        }
        this.registerForm = this.registerForm.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }
    registerForm(e){
        this.setState({
            name: e.target.name,
            age: e.target.age,
            email: e.target.email,
            tel: e.target.tel
        })
    }
    handleSubmit(event) {
        alert('Отправленное имя: ' + this.state.name)
        event.preventDefault()
      }
    render(){
        return(
            <main>
        <div className="registr-hold">
            <h1>
                Регистрация 
            </h1>
        </div>
        <form action="vacansi" onSubmit={this.handleSubmit}>
            <div className="info">
                <h2>Основная информация</h2>
                <hr className="hr"/>
            </div>
            
            <div className="nam">
                <label for="name">Имя:</label>
                <input type="text" id="name" 
                value={this.state.name} 
                onChange={this.registerForm}/>
                <hr/>
            </div>
            <div className="nam">
                <label for="old">Возраст:</label>
                <input type="text" id="old"  
                value={this.state.age}
                onChange={this.registerForm}/>
                <hr/>
            </div>
            <div className="nam">
                <label for="e-mail">E-mail:</label>
                <input type="text" id="e-mail"  value={this.state.email}
                onChange={
                    this.registerForm
                }/>
                <hr/>
                <div className="checbox">
                    <input type="checkbox" id="chec"/>
                    <label for="chec" style={{fontSize: 15+"px", fontWeight: 100}}>
                        Получать дополнительную информацию</label>
                </div>
            </div>
            <div className="nam">
                <label for="tel">Телефон:</label>
                <input type="tel" id="tel"  value={this.state.tel}
                onChange={this.registerForm}/>
                <hr/>
            </div>
            <input type="submit" value="Продолжить"  className="btn-register-page"/> 
        </form>  
        <img src="/asset/registr.svg" alt="" className="img-registr"/>  
    </main>
        )
    }
}

export default Register;