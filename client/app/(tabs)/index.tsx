import { Image, StyleSheet, Platform, SafeAreaView } from "react-native";
import { StatusBar } from "expo-status-bar";
import ClanMemberTable from "@/components/ClanMemberTable";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
});

export default function HomeScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <ClanMemberTable />
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}
