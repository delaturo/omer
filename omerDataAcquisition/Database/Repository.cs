using omerDataAcquisition.Models;
using System.Text.Json;

namespace omerDataAcquisition.Database{
    public class Repository{
        /* Connection object */

        public CharStatus getCharStatus(string c){
            return null;
        }

        public CharStatus[] getAllCharStatus(){
            return null;
        }

        public static CharStatus getRandomChar(){
            string jsonRes = DBContext.getDBInstance().requestRandChar();
            CharStatus cs = JsonSerializer.Deserialize<CharStatus>(jsonRes);
            return cs;
        }

        public static void saveCapture(int charId, byte[] capture){
            HWChar charcap = new HWChar();
            charcap.char_id = charId;
            charcap.img = capture;
            DBContext.getDBInstance().saveCapture(charcap);
            return;
        }
    }
}