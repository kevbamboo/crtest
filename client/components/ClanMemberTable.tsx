import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ActivityIndicator,
} from "react-native";
import axios from "axios";

const ClanMemberTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortConfig, setSortConfig] = useState({ key: null, direction: "asc" });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:8080/api/daysInactive"
        );
        setData(response.data);
        setLoading(false);
      } catch (err: any) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleSort = (key: any) => {
    // TODO change type
    let direction = "asc";
    if (sortConfig.key === key && sortConfig.direction === "asc") {
      direction = "desc";
    }
    setSortConfig({ key, direction });
  };

  const sortedData = () => {
    if (!sortConfig.key) return data;

    return [...data].sort((a: any, b: any) => {
      if (sortConfig.key === "name") {
        return sortConfig.direction === "asc"
          ? a.name.localeCompare(b.name)
          : b.name.localeCompare(a.name);
      }
      if (sortConfig.key === "daysInactive") {
        return sortConfig.direction === "asc"
          ? a.inactive_days - b.inactive_days
          : b.inactive_days - a.inactive_days;
      }
      return 0;
    });
  };

  if (loading) {
    return <ActivityIndicator size="large" style={styles.loader} />;
  }

  if (error) {
    return <Text style={styles.error}>Error: {error}</Text>;
  }

  return (
    <View style={styles.container}>
      <View style={styles.headerRow}>
        <TouchableOpacity
          style={styles.headerCell}
          onPress={() => handleSort("name")}
        >
          <Text style={styles.headerText}>
            Name{" "}
            {sortConfig.key === "name" &&
              (sortConfig.direction === "asc" ? "↑" : "↓")}
          </Text>
        </TouchableOpacity>

        <View style={styles.headerCell}>
          <Text style={styles.headerText}>Tag</Text>
        </View>

        <TouchableOpacity
          style={styles.headerCell}
          onPress={() => handleSort("daysInactive")}
        >
          <Text style={styles.headerText}>
            Last Seen{" "}
            {sortConfig.key === "daysInactive" &&
              (sortConfig.direction === "asc" ? "↑" : "↓")}
          </Text>
        </TouchableOpacity>
      </View>

      {sortedData().map((member: any, index: any) => (
        <View key={index} style={styles.dataRow}>
          <View style={styles.dataCell}>
            <Text>{member.name}</Text>
          </View>
          <View style={styles.dataCell}>
            <Text>{member.tag}</Text>
          </View>
          <View style={styles.dataCell}>
            <Text>{member.inactive_days}</Text>
          </View>
        </View>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: "#fff",
  },
  loader: {
    marginTop: 20,
  },
  error: {
    color: "red",
    padding: 20,
    textAlign: "center",
  },
  headerRow: {
    flexDirection: "row",
    borderBottomWidth: 1,
    borderColor: "#ddd",
    paddingBottom: 8,
    marginBottom: 8,
  },
  headerCell: {
    flex: 1,
    alignItems: "center",
    padding: 8,
  },
  headerText: {
    fontWeight: "bold",
  },
  dataRow: {
    flexDirection: "row",
    borderBottomWidth: 1,
    borderColor: "#eee",
    paddingVertical: 8,
  },
  dataCell: {
    flex: 1,
    alignItems: "center",
    padding: 4,
  },
});

export default ClanMemberTable;
