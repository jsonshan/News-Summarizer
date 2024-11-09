import { useState , useEffect } from 'react'
import './App.css'
import TextBlock from './components/TextBlock'
import NewsSource from './components/NewsSource'
import GenreSelection from './components/GenreSelection'


function App() {
  const [sources, setSources] = useState([['https://yt3.googleusercontent.com/n5DRh94eycw6xGcOKTn6LKQwztTwaw24fXPniFTXA3VPgwJaiOFdBwJNtXRHYUf7OdEAk9upwH0=s900-c-k-c0x00ffffff-no-rj', 'CNN'], ['https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/1280px-Fox_News_Channel_logo.svg.png', 'Fox News'], ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyVD42A8Qq2LuigyjvjH07iS-9xTALFaQDgw&s', 'NBC'], ['https://api.time.com/wp-content/themes/time2014/img/time-logo-og.png', 'TIME'], ['https://pbs.twimg.com/profile_images/1707446114717429760/Bt3mH-ZU_400x400.jpg', 'CBS']])
  const [selectedPage, setSelectedPage] = useState('technology');
  const [genres, setGeneres] = useState(['Finance', 'Politics', 'World', 'Health', 'Business', 'Environment', 'Tech', 'Entertainment', 'Science', 'History', 'Sports']);

  const[selectedSources, setSelectedSources] = useState([true, true, true, true, true, true])
  const [selectedGenre, setSelectedGenre] = useState('Finance');
  const updateSources = (data) => {
    setSelectedSources(data);
    // console.log("new sources ", data);
  }
  const handleChangeGenre = (genre) => {
    setSelectedGenre(genre);
    // console.log("new genre  ", genre);
  }
  useEffect(() => {
    console.log('Updated selectedSources:', selectedSources);
  }, [selectedSources, selectedGenre]);

  return (
    <>
      <div className='App'> {/* main page */}
        <h1 id="page-title">WEB TITLE PLACEHOLDER</h1>
        <h3 className="sub-title">News Sources</h3>
        <NewsSource sources={sources} onChangeSelected={updateSources}/>
        <h3 className="genre-title">Genre</h3>
        <GenreSelection genres={genres} onChangeGenre={handleChangeGenre}></GenreSelection>
        <h3 className="sub-title">Summary</h3>
        <TextBlock type="main-summary"/>
        <h3 className="sub-title">Summary (Separate Sources)</h3>
        <TextBlock type="sub-summary" logo='https://yt3.googleusercontent.com/n5DRh94eycw6xGcOKTn6LKQwztTwaw24fXPniFTXA3VPgwJaiOFdBwJNtXRHYUf7OdEAk9upwH0=s900-c-k-c0x00ffffff-no-rj' srcName="CNN"/>
      </div>
    </>
  )
}

export default App
