import React, { Component } from "react";
import Card from "./Card";

class Generate extends Component {
  state = {
    pokename: "pikachu",
    pic: "",
    hp: 60,
    type: "electric",
    attack: 60,
    defence: 60,
    speed: 60,
  };

  getPokeData = async () => {
    const id = Math.floor(Math.random() * 150) + 1;
    const url = `https://pokeapi.co/api/v2/pokemon/${id}`;

    const response = await fetch(url);
    const data = await response.json();
    this.setState({
      pokename: data.name,
      hp: data.stats[0].base_stat,
      pic: data.sprites.other.dream_world.front_default,
      attack: data.stats[1].base_stat,
      defence: data.stats[2].base_stat,
      speed: data.stats[5].base_stat,
      type: data.types[0].type.name,
    });
  };

  render() {
    return (
      <div>
        <Card
          key={this.state.pokename}
          pokename={this.state.pokename}
          pic={this.state.pic}
          hp={this.state.hp}
          attack={this.state.attack}
          defence={this.state.defence}
          speed={this.state.speed}
          type={this.state.type}
        />
        <button className="btn" onClick={this.getPokeData}></button>
        
      </div>
    );
  }
}

export default Generate;
