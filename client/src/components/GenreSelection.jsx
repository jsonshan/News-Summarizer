
import React, {useEffect} from 'react'
import "../styles/GenreSelection.css"


function GenreSelection({genres}) {
  function select(genreName) {
    genres.forEach((element) => {
      let item = document.getElementById(element);
      let x = document.getElementById(genreName);
      if (element === genreName) x.classList.add("enabled");
      else item.classList.remove("enabled");
    });
  }

  useEffect(() => {
    // Set "finance" as the initial genre with the "enabled" class
    if (genres.includes("finance")) {
      select("finance");
    }
  }, [genres]); // Only runs when 'genres' changes

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