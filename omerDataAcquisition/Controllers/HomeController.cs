using System;
using System.Diagnostics;
using System.Text.Json;
using System.IO;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using omerDataAcquisition.Models;
using omerDataAcquisition.Database;

namespace omerDataAcquisition.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            CharStatus cs = Repository.getRandomChar();
            return View(cs);
        }

        public IActionResult Info()
        {
            return View();
        }

        public IActionResult Status(){
            CharStatus []charStatus = Repository.getAllCharStatus();
            ViewData["charsStatus"] = JsonSerializer.Serialize<CharStatus[]>(charStatus);
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

        [HttpPost]
        public string SaveCapture(int charId, string imgCaptured){
            String imgTempName = Path.GetTempPath() + Guid.NewGuid().ToString() + ".png";
             using(FileStream fs = new FileStream(imgTempName, FileMode.Create)) {
                using(BinaryWriter bw = new BinaryWriter(fs)) {
                    byte[] data = Convert.FromBase64String(imgCaptured);
                    bw.Write(data);
                    bw.Close();
                }
            }
            
            using (Stream fs = new FileStream(imgTempName, FileMode.Open)){
                using (BinaryReader br = new BinaryReader(fs)){
                    byte[] bytes = br.ReadBytes((Int32)fs.Length);
                    Repository.saveCapture(charId, bytes);
                }
            }

            return "Done!!";
        }
    }
}
