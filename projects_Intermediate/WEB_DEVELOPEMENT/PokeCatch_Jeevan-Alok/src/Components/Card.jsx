import React, { Component } from "react";
import attack from "../images/battle.png";
import defence from "../images/shield1.png";
import speed from "../images/speed.png";
import health from "../images/life.png";

class Card extends Component {
  render() {
    return (
      <div className={`cards typeColor-${this.props.type}`}>
        <div className="hp">
          <img src={health} alt="" /> <span>{this.props.hp}</span>
        </div>
        <img className="pokepic" src={this.props.pic} alt="" />
        <h2 className="poke-name">{this.props.pokename}</h2>
        <div className="types">
          <span className={`${this.props.type}`}>{this.props.type}</span>
        </div>
        <div className="stats">
          <div className="box">
            <img className="pokeball" src={attack} />
            <h3>{this.props.attack}</h3>
          </div>
          <div className="box">
            <img className="pokeball" src={defence} />
            <h3>{this.props.defence}</h3>
          </div>
          <div className="box">
            <img className="pokeball" src={speed} />
            <h3>{this.props.speed}</h3>
          </div>
        </div>
      </div>
    );
  }
}

export default Card;
