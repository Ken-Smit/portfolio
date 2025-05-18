import React, { useState, useEffect } from 'react';
import { Text, View, Button } from 'react-native';
import { AppleMusicAPI } from 'apple-music-api-react-native';
import { SpotifyAPI } from 'spotify-api-react-native';
import { GroqClient } from 'groq-client-react-native';

const App = () => {
  const [musicService, setMusicService] = useState('apple_music');
  const [ Token, setToken] = useState('');
  const [data, setData] = useState({});

  useEffect(() => {
    if (musicService === 'apple_music') {
      AppleMusicAPI.authenticate().then((token) => {
        setToken(token);
      });
    } else {
      SpotifyAPI.authenticate().then((token) => {
        setToken(token);
      });
    }
  }, [musicService]);

  const fetchMusicData = () => {
    if (musicService === 'apple_music') {
      AppleMusicAPI.fetchTopSongs(Token).then((data) => {
        setData(data);
      });
    } else {
      SpotifyAPI.fetchNewReleases(Token).then((data) => {
        setData(data);
      });
    }
  };

  const analyzeMusicData = () => {
    const groqClient = new GroqClient();
    const query = `analyze ${data}`;
    groqClient.query(query).then((result) => {
      console.log(result);
    });
  };

  return (
    <View>
      <Text>Select Music Service:</Text>
      <Button title="Apple Music" onPress={() => setMusicService('apple_music')} />
      <Button title="Spotify" onPress={() => setMusicService('spotify')} />
      <Button title="Fetch Music Data" onPress={fetchMusicData} />
      <Button title="Analyze Music Data" onPress={analyzeMusicData} />
      <Text>Data: {data}</Text>
    </View>
  );
};

export default App;