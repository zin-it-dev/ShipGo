import { View, Text } from "react-native";
import React from "react";
import { useQuery } from "@tanstack/react-query";

import axios from "@/libs/configs/axios";

const Home = () => {
  const { data, isLoading, error } = useQuery({
    queryKey: ["categories"],
    queryFn: async () => {
      const response = await axios.get("/categories/");
      return response.data;
    },
  });

  console.log(process.env.EXPO_PUBLIC_API_URL);

  if (isLoading) return <Text>Loading...</Text>;
  if (error) return <Text>Error: {error.message}</Text>;

  return (
    <View>
      <Text>Home</Text>
      <Text>{JSON.stringify(data)}</Text>;
    </View>
  );
};

export default Home;
