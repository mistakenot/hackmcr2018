using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using web.Models;

namespace web.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult IndexPost(HomeSubmitModel model)
        {
            var registerModel = new RegisterModel
            {
                From = model.From,
                To = model.To,
                Price = 9.0m
            };

            return View("Register", registerModel);
        }

        public IActionResult Register(RegisterModel model)
        {
            string[] zones = { "Unsociable", "Third-Class", "First-Class", "Sick", "Noisy" };
            string[] messages = {
                "You like people",
                "You are too rich",
                "You spend too little",
                "You look after yourself too much",
                "You like peace and quiet"};

            Random rnd = new Random();
            int value = rnd.Next(0,5);

            // Get data here.
            var dataModel = new DataResults
            {
                Name = model.firstNameInput + " " + model.lastNameInput,
                Zone = zones[value],
                Message = messages[value]
            };

            return View("Confirmation", dataModel);
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";

            return View();
        }

        public IActionResult Contact()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}