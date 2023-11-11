import { StyleSheet, Text, View } from "react-native";
import { useEffect, useState } from "react";

import { StatusBar } from "expo-status-bar";
import axios from "axios";

const axiosInstance = axios.create({ baseURL: "http://127.0.0.1:5000" });

export default function App() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    axiosInstance.get("/todos").then((response) => setTodos(response.data));
  }, []);

  console.log(todos);

  return (
    <View style={styles.container}>
      <Text>{todos.length ? todos.length : "None"}</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
