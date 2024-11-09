import React from 'react'
import "../styles/GenreSelection.css"


function GenreSelection({genres}) {


  function select(genreName){
    genres.forEach((element) => {
      let item = document.getElementById(element);
      let x = document.getElementById(genreName);
      if(element === genreName) x.classList.add("enabled");
      else item.classList.remove("enabled");
    })
  }
  
  // function selected(element){
  //   let item = document.getElementById(element);
  //   item.classList.add("enabled");
  // }

  return (
    <div className="genre-container">
      <div className="genre-wrapper">
        {genres.map((i, j) => {
          return <div className="genre-cards" id = {i} key={j} onClick = {() => {select(i)}}>{i}</div>
        })}
      </div>
    </div>
  )
}

export default GenreSelection