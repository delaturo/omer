using System;
using omerDataAcquisition.Models;
using System.Data.SqlClient;
using MySqlConnector;

namespace omerDataAcquisition.Database{
    public class DBContext{
        private static DBContext dbInstance;
        private string strConnection { get; set; }


        public static void config(string connectionString){
            dbInstance = new DBContext(connectionString);
        }

        public static DBContext getDBInstance(){
            if (dbInstance == null){
                throw new InvalidOperationException("DB connection not configured");
            }else{
                return dbInstance;
            }
        }

        private DBContext(string connectionString){
            strConnection = connectionString;
        }

        private MySqlConnection generateConnection(){            
            var builder = new MySqlConnectionStringBuilder(strConnection);
            return new MySqlConnection(builder.ConnectionString);;
        }

        public string requestCharStatus(string c){
            string res = "";
            string query = "SELECT id, letter, utf8_val, count FROM charstatus";
            if (c != null){
                query += "WHERE letter=" + c;
            }
            using (MySqlConnection conn = generateConnection()){
                conn.Open();
                using (MySqlCommand cmd = new MySqlCommand(query,conn)){
                    using(MySqlDataReader reader =cmd.ExecuteReader()){
                        while(reader.Read()){
                            var r = "{" + "id:\"" + reader.GetString(0) + "\"" + ",letter:\"" + reader.GetString(1) + "\""
                             + ",utf8_val:\"" + reader.GetString(2) + "\"" + ",count:\"" + reader.GetString(3) + "\"" + "}";
                             res = r + "\n";
                        }
                        res = "{\n" + res + "}";
                    }
                }
            }
            return res;
        }

        public string requestRandChar(){
            string res = "";
            string query = "SELECT id, letter, utf8_val, count, name FROM nextchar";
            using (MySqlConnection conn = generateConnection()){
                conn.Open();
                using (MySqlCommand cmd = new MySqlCommand(query,conn)){
                    using(MySqlDataReader reader =cmd.ExecuteReader()){
                        while(reader.Read()){
                            res = "{\"id\":" + reader.GetInt64(0) + ",\"letter\":\"" + reader.GetString(1) + "\""
                             + ",\"utf8_val\":" + reader.GetInt64(2) + ",\"count\":" + reader.GetInt64(3) +
                             ", \"name\":\"" + reader.GetString(4) + "\"}";
                        }
                    }
                }
            }
            return res;
        }

        public void saveCapture(HWChar capture){
            string query = "INSERT INTO capture (char_id, img) VALUES (@charId, @capture);";
            using (MySqlConnection conn = generateConnection()){
                conn.Open();
                using (MySqlCommand cmd = new MySqlCommand(query,conn)){
                    cmd.Parameters.Add("@charId", MySqlDbType.Int64).Value = capture.char_id;
                    cmd.Parameters.Add("@capture", MySqlDbType.LongBlob).Value = capture.img;
                    cmd.ExecuteNonQuery();
                }
            }
        }
    }
}