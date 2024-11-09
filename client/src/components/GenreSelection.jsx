
import React, {useEffect} from 'react'
import "../styles/GenreSelection.css"


function GenreSelection({genres, onChangeGenre}) {
  function select(genreName) {
    onChangeGenre(genreName);
    genres.forEach((element) => {
      let item = document.getElementById(element);
      let x = document.getElementById(genreName);
      if (element === genreName) x.classList.add("enabled");
      else item.classList.remove("enabled");
    });
  }

  useEffect(() => {
    if (genres.includes("Finance")) {
      select("Finance");
    }
  }, [genres]);

  return (
    <div className="genre-container">
      <div className="genre-wrapper">
        {genres.map((i, j) => {
          return <div className="genre-cards" id = {i} key={j} onClick = {() => {select(i)}}> {i}  
          </div>
        })}
      </div>
    </div>
  )
}

export default GenreSelection