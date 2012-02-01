using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Zentity.Core;
using System.Xml.Serialization;using Zentity.Corel52;
namespace DataInsert
{ 
 	 class DataInsert 
 	 { 
   
 		 /// <summary> 
 		 /// Deserializes the specified XML path. 
 		 /// </summary> 
 		 /// <typeparam name="T"></typeparam> 
 		 /// <param name="xmlPath">The XML path.</param> 
 		 /// <returns></returns> 
 		 private static T Deserialize<T>(string xmlPath) 
 		 { 
 			 XmlSerializer xmlSerializer = new XmlSerializer(typeof(T)); 
 			 using (StreamReader xmlStream = new StreamReader(xmlPath)) 
 			 { 
 				 T tempObject = (T)xmlSerializer.Deserialize(xmlStream); 
 				 return tempObject; 
 			 } 
 		 } 
 		 /// <summary> 
 		 /// method for converting a UNIX timestamp to a regular 
 		  ///System.DateTime value (and also to the current local time) 
 		  ///</summary> 
 		  ///<param name="timestamp">value to be converted</param> 
 		  ///<returns>converted DateTime in string format</returns> 
 		 private static DateTime ConvertTimestamp(double timestamp) 
 		 { 
 			 //create a new DateTime value based on the Unix Epoch 
 			DateTime converted = new DateTime(1970, 1, 1, 0, 0, 0, 0); 
 			//add the timestamp to the value 
 			DateTime newDateTime = converted.AddSeconds(timestamp); 
 			//return the value in string format 
 			return newDateTime.ToLocalTime(); 
 		 } 
 		 private ParentImages dataParentImages; 
 		 private void loadParentImagesData(string xmlPath) 
 		 { 
 			dataParentImages= Deserialize<ParentImages>(xmlPath); 
 		 } 
 		 public void insertData_Corel5Image2(ZentityContext zenContext, string xmlPath, string imgPath) 
 		 { 
 			 loadParentImagesData(xmlPath); 
 			 using (ZentityContext context = zenContext) 
 			 { 
 				 foreach (ParentImagesImage p in dataParentImages.Items) 
 				 { 
 					 //WARNING : Comparing attribute should be changed to a unique key 
 					 context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("Zentity.Corel52")); 
 					 var existingPres = (from pres in context.Resources 
 						 where pres.ImageID.Equals(p.ImageID, StringComparison.OrdinalIgnoreCase) 
 						 select pres).FirstOrDefault(); 
 						 if (existingPres != null) 
 						 { 
 							 Console.WriteLine("[WARNING] Image {0} already exists in database", p.ImageID); 
 							 continue; 
 						 } 
 						 // Create resources. 
 						 try 
 							 { 
 							 Corel5Image2 img = new Corel5Image2 {
 								  Title = p.Title,
 								  Description = p.Description,
 								  Main_Textual_Category = p.Main_Textual_Category,
 								  Main_Visual_Category = p.Main_Visual_Category,
 								  ImageID = p.ImageID,
 								  LTT_hills_dunes_road_canyon_antelope_caribou_palace = Convert.ToDouble(p.LTT_hills_dunes_road_canyon_antelope_caribou_palace),
 								  LTT_sunset_horizon_desert_valley_landscape_sunrise_palm = Convert.ToDouble(p.LTT_sunset_horizon_desert_valley_landscape_sunrise_palm),
 								  LTT_water_reflection_shore_zebra_park_restaurant_herd = Convert.ToDouble(p.LTT_water_reflection_shore_zebra_park_restaurant_herd),
 								  LTT_plane_jet_runway_smoke_f__16_prop_zebra = Convert.ToDouble(p.LTT_plane_jet_runway_smoke_f__16_prop_zebra),
 								  LTT_harbor_tower_water_sky_ships_windmills_town = Convert.ToDouble(p.LTT_harbor_tower_water_sky_ships_windmills_town),
 								  LTT_window_door_castle_courtyard_farms_tables_palace = Convert.ToDouble(p.LTT_window_door_castle_courtyard_farms_tables_palace),
 								  LTT_field_tulip_bulls_elk_row_farms_vineyard = Convert.ToDouble(p.LTT_field_tulip_bulls_elk_row_farms_vineyard),
 								  LTT_coast_waves_water_town_lighthouse_park_fog = Convert.ToDouble(p.LTT_coast_waves_water_town_lighthouse_park_fog),
 								  LTT_swimmers_people_athlete_pool_interior_wings_chairs = Convert.ToDouble(p.LTT_swimmers_people_athlete_pool_interior_wings_chairs),
 								  LTT_cat_tiger_forest_bengal_head_ground_lynx = Convert.ToDouble(p.LTT_cat_tiger_forest_bengal_head_ground_lynx),
 								  LTT_bear_polar_tundra_black_grizzly_cubs_ice = Convert.ToDouble(p.LTT_bear_polar_tundra_black_grizzly_cubs_ice),
 								  LTT_sun_sea_waves_land_bay_lake_sunrise = Convert.ToDouble(p.LTT_sun_sea_waves_land_bay_lake_sunrise),
 								  LTT_tree_forest_park_frost_elk_palace_deer = Convert.ToDouble(p.LTT_tree_forest_park_frost_elk_palace_deer),
 								  LTT_island_village_water_face_formation_farms_ships = Convert.ToDouble(p.LTT_island_village_water_face_formation_farms_ships),
 								  LTT_temple_pillar_roofs_buddha_buddhist_mosque_road = Convert.ToDouble(p.LTT_temple_pillar_roofs_buddha_buddhist_mosque_road),
 								  LTT_house_roofs_hut_village_fence_lawn_town = Convert.ToDouble(p.LTT_house_roofs_hut_village_fence_lawn_town),
 								  LTT_beach_palm_sand_oahu_kauai_sunset_hawaii = Convert.ToDouble(p.LTT_beach_palm_sand_oahu_kauai_sunset_hawaii),
 								  LTT_snow_fox_polar_coyote_head_arctic_deer = Convert.ToDouble(p.LTT_snow_fox_polar_coyote_head_arctic_deer),
 								  LTT_river_water_fox_elk_autumn_coyote_antlers = Convert.ToDouble(p.LTT_river_water_fox_elk_autumn_coyote_antlers),
 								  LTT_pool_hotel_town_water_swimmers_maui_people = Convert.ToDouble(p.LTT_pool_hotel_town_water_swimmers_maui_people),
 								  LTT_bridge_arch_steel_stone_train_courtyard_architecture = Convert.ToDouble(p.LTT_bridge_arch_steel_stone_train_courtyard_architecture),
 								  LTT_sand_valley_desert_dunes_pyramid_canyon_sailboats = Convert.ToDouble(p.LTT_sand_valley_desert_dunes_pyramid_canyon_sailboats),
 								  LTT_train_railroad_locomotive_smoke_tracks_close__up_bridge = Convert.ToDouble(p.LTT_train_railroad_locomotive_smoke_tracks_close__up_bridge),
 								  LTT_clouds_palace_ruins_tower_park_buddhist_pyramid = Convert.ToDouble(p.LTT_clouds_palace_ruins_tower_park_buddhist_pyramid),
 								  LTT_ice_frost_frozen_crystals_fruit_glass_stick = Convert.ToDouble(p.LTT_ice_frost_frozen_crystals_fruit_glass_stick),
 								  LTT_sky_flight_roofs_prop_castle_church_park = Convert.ToDouble(p.LTT_sky_flight_roofs_prop_castle_church_park),
 								  LTT_mountain_valley_desert_park_ruins_road_goat = Convert.ToDouble(p.LTT_mountain_valley_desert_park_ruins_road_goat),
 								  LTT_city_skyline_night_light_landscape_tower_church = Convert.ToDouble(p.LTT_city_skyline_night_light_landscape_tower_church),
 								  LTT_rocks_fox_canyon_valley_rodent_tortoise_giant = Convert.ToDouble(p.LTT_rocks_fox_canyon_valley_rodent_tortoise_giant),
 								  LTT_stone_ruins_sculpture_pyramid_pillar_road_relief = Convert.ToDouble(p.LTT_stone_ruins_sculpture_pyramid_pillar_road_relief),
 								  LTT_water_grizzly_tusks_horizon_ground_bear_canal = Convert.ToDouble(p.LTT_water_grizzly_tusks_horizon_ground_bear_canal),
 								  LTT_boats_water_skyline_market_maui_restaurant_paintings = Convert.ToDouble(p.LTT_boats_water_skyline_market_maui_restaurant_paintings),
 								  LTT_cars_tracks_turn_prototype_formula_straightaway_close__up = Convert.ToDouble(p.LTT_cars_tracks_turn_prototype_formula_straightaway_close__up),
 								  LTT_scotland_town_castle_village_cottage_church_mountain = Convert.ToDouble(p.LTT_scotland_town_castle_village_cottage_church_mountain),
 								  LTT_grass_zebra_fox_herd_ground_antlers_caribou = Convert.ToDouble(p.LTT_grass_zebra_fox_herd_ground_antlers_caribou),
 								  LTT_wall_formula_church_castle_sign_writing_facade = Convert.ToDouble(p.LTT_wall_formula_church_castle_sign_writing_facade),
 								  LTT_people_woman_indian_hats_costume_girl_monks = Convert.ToDouble(p.LTT_people_woman_indian_hats_costume_girl_monks),
 								  LTT_ocean_coral_reefs_fish_sea_anemone_fan = Convert.ToDouble(p.LTT_ocean_coral_reefs_fish_sea_anemone_fan),
 								  LTT_buildings_skyline_village_hotel_flag_roofs_light = Convert.ToDouble(p.LTT_buildings_skyline_village_hotel_flag_roofs_light),
 								  LTT_shops_market_display_food_sign_restaurant_writing = Convert.ToDouble(p.LTT_shops_market_display_food_sign_restaurant_writing),
 								  LTT_branch_tree_sign_shrubs_leopard_elephant_blossoms = Convert.ToDouble(p.LTT_branch_tree_sign_shrubs_leopard_elephant_blossoms),
 								  LTT_plants_leaf_close__up_stems_head_palm_lily = Convert.ToDouble(p.LTT_plants_leaf_close__up_stems_head_palm_lily),
 								  LTT_statue_sculpture_palace_sphinx_figures_buddha_castle = Convert.ToDouble(p.LTT_statue_sculpture_palace_sphinx_figures_buddha_castle),
 								  LTT_water_cliff_white__tailed_deer_fountain_people_marine = Convert.ToDouble(p.LTT_water_cliff_white__tailed_deer_fountain_people_marine),
 								  LTT_garden_lawn_landscape_flowers_path_bench_palace = Convert.ToDouble(p.LTT_garden_lawn_landscape_flowers_path_bench_palace),
 								  LTT_horses_foals_mare_fence_field_town_guard = Convert.ToDouble(p.LTT_horses_foals_mare_fence_field_town_guard),
 								  LTT_people_man_pillar_ceremony_courtyard_umbrella_kauai = Convert.ToDouble(p.LTT_people_man_pillar_ceremony_courtyard_umbrella_kauai),
 								  LTT_street_town_cars_skyline_guard_sign_buildings = Convert.ToDouble(p.LTT_street_town_cars_skyline_guard_sign_buildings),
 								  LTT_birds_nest_flight_booby_fly_albatross_wood = Convert.ToDouble(p.LTT_birds_nest_flight_booby_fly_albatross_wood),
 								  LTT_flowers_petals_leaf_tulip_stems_poppies_blooms = Convert.ToDouble(p.LTT_flowers_petals_leaf_tulip_stems_poppies_blooms),
 								  LTV_water_sky_people_mountain_beach_waves_rocks = Convert.ToDouble(p.LTV_water_sky_people_mountain_beach_waves_rocks),
 								  LTV_tree_grass_field_horses_foals_mare_train = Convert.ToDouble(p.LTV_tree_grass_field_horses_foals_mare_train),
 								  LTV_snow_cars_tracks_wall_tree_formula_frost = Convert.ToDouble(p.LTV_snow_cars_tracks_wall_tree_formula_frost),
 								  LTV_water_snow_polar_bear_stone_tracks_cars = Convert.ToDouble(p.LTV_water_snow_polar_bear_stone_tracks_cars),
 								  LTV_ruins_stone_tree_water_snow_scotland_mountain = Convert.ToDouble(p.LTV_ruins_stone_tree_water_snow_scotland_mountain),
 								  LTV_tusks_ground_water_sand_valley_sky_dunes = Convert.ToDouble(p.LTV_tusks_ground_water_sand_valley_sky_dunes),
 								  LTV_people_buildings_sky_sunset_tree_night_city = Convert.ToDouble(p.LTV_people_buildings_sky_sunset_tree_night_city),
 								  LTV_garden_ruins_tree_people_stone_sky_wall = Convert.ToDouble(p.LTV_garden_ruins_tree_people_stone_sky_wall),
 								  LTV_sky_flowers_mountain_people_clouds_water_leaf = Convert.ToDouble(p.LTV_sky_flowers_mountain_people_clouds_water_leaf),
 								  LTV_sky_jet_plane_train_railroad_tree_pool = Convert.ToDouble(p.LTV_sky_jet_plane_train_railroad_tree_pool),
 								  LTV_water_grass_bear_polar_mist_dunes_cubs = Convert.ToDouble(p.LTV_water_grass_bear_polar_mist_dunes_cubs),
 								  LTV_sky_jet_plane_mountain_sand_snow_valley = Convert.ToDouble(p.LTV_sky_jet_plane_mountain_sand_snow_valley),
 								  LTV_sky_jet_plane_water_tree_bridge_pool = Convert.ToDouble(p.LTV_sky_jet_plane_water_tree_bridge_pool),
 								  LTV_sky_plane_jet_eagle_flight_mountain_birds = Convert.ToDouble(p.LTV_sky_plane_jet_eagle_flight_mountain_birds),
 								  LTV_sky_plane_jet_tree_mountain_bridge_castle = Convert.ToDouble(p.LTV_sky_plane_jet_tree_mountain_bridge_castle),
 								  LTV_plane_jet_sky_clouds_sand_valley_beach = Convert.ToDouble(p.LTV_plane_jet_sky_clouds_sand_valley_beach),
 								  LTV_grass_sky_tree_water_rocks_rodent_bear = Convert.ToDouble(p.LTV_grass_sky_tree_water_rocks_rodent_bear),
 								  LTV_sky_jet_plane_mountain_water_park_buildings = Convert.ToDouble(p.LTV_sky_jet_plane_mountain_water_park_buildings),
 								  LTV_sky_plane_mountain_prop_tree_palace_water = Convert.ToDouble(p.LTV_sky_plane_mountain_prop_tree_palace_water),
 								  LTV_sky_clouds_plane_jet_train_railroad_locomotive = Convert.ToDouble(p.LTV_sky_clouds_plane_jet_train_railroad_locomotive),
 								  LTV_sky_jet_plane_water_valley_desert_sand = Convert.ToDouble(p.LTV_sky_jet_plane_water_valley_desert_sand),
 								  LTV_bear_snow_polar_ice_people_water_tracks = Convert.ToDouble(p.LTV_bear_snow_polar_ice_people_water_tracks),
 								  LTV_sky_plane_jet_tree_mountain_clouds_valley = Convert.ToDouble(p.LTV_sky_plane_jet_tree_mountain_clouds_valley),
 								  LTV_water_sunset_coast_horizon_sun_tree_clouds = Convert.ToDouble(p.LTV_water_sunset_coast_horizon_sun_tree_clouds),
 								  LTV_tree_people_sky_buildings_water_rocks_mountain = Convert.ToDouble(p.LTV_tree_people_sky_buildings_water_rocks_mountain),
 								  LTV_snow_water_sky_bear_stone_polar_sand = Convert.ToDouble(p.LTV_snow_water_sky_bear_stone_polar_sand),
 								  LTV_water_people_swimmers_pool_tree_plants_leaf = Convert.ToDouble(p.LTV_water_people_swimmers_pool_tree_plants_leaf),
 								  LTV_tree_water_sky_mountain_buildings_people_rocks = Convert.ToDouble(p.LTV_tree_water_sky_mountain_buildings_people_rocks),
 								  LTV_tree_flowers_rose_frost_ice_plants_mountain = Convert.ToDouble(p.LTV_tree_flowers_rose_frost_ice_plants_mountain),
 								  LTV_sky_birds_flight_eagle_mountain_snow_clouds = Convert.ToDouble(p.LTV_sky_birds_flight_eagle_mountain_snow_clouds),
 								  LTV_sky_jet_plane_branch_birds_sand_tree = Convert.ToDouble(p.LTV_sky_jet_plane_branch_birds_sand_tree),
 								  LTV_cars_tracks_ice_water_formula_wall_turn = Convert.ToDouble(p.LTV_cars_tracks_ice_water_formula_wall_turn),
 								  LTV_mountain_tree_bridge_sky_water_clouds_arch = Convert.ToDouble(p.LTV_mountain_tree_bridge_sky_water_clouds_arch),
 								  LTV_people_temple_scotland_stone_grass_water_pillar = Convert.ToDouble(p.LTV_people_temple_scotland_stone_grass_water_pillar),
 								  LTV_sand_people_close__up_lizard_grass_tree_field = Convert.ToDouble(p.LTV_sand_people_close__up_lizard_grass_tree_field),
 								  LTV_sand_stone_rocks_polar_bear_sky_snow = Convert.ToDouble(p.LTV_sand_stone_rocks_polar_bear_sky_snow),
 								  LTV_water_sky_jet_mountain_plane_train_buildings = Convert.ToDouble(p.LTV_water_sky_jet_mountain_plane_train_buildings),
 								  LTV_flowers_tree_birds_grass_leaf_plants_nest = Convert.ToDouble(p.LTV_flowers_tree_birds_grass_leaf_plants_nest),
 								  LTV_water_sky_grass_people_tree_mountain_snow = Convert.ToDouble(p.LTV_water_sky_grass_people_tree_mountain_snow),
 								  LTV_people_polar_bear_face_water_snow_buildings = Convert.ToDouble(p.LTV_people_polar_bear_face_water_snow_buildings),
 								  LTV_leaf_plants_flowers_garden_birds_tree_nest = Convert.ToDouble(p.LTV_leaf_plants_flowers_garden_birds_tree_nest),
 								  LTV_buildings_people_city_water_sky_statue_night = Convert.ToDouble(p.LTV_buildings_people_city_water_sky_statue_night),
 								  LTV_stone_pillar_sculpture_people_statue_tree_road = Convert.ToDouble(p.LTV_stone_pillar_sculpture_people_statue_tree_road),
 								  LTV_sky_water_sand_beach_people_hills_tree = Convert.ToDouble(p.LTV_sky_water_sand_beach_people_hills_tree),
 								  LTV_sky_jet_plane_train_railroad_locomotive_pagoda = Convert.ToDouble(p.LTV_sky_jet_plane_train_railroad_locomotive_pagoda),
 								  LTV_jet_plane_sky_beach_boats_steel_courtyard = Convert.ToDouble(p.LTV_jet_plane_sky_beach_boats_steel_courtyard),
 								  LTV_plane_sky_prop_bridge_valley_boats_sand = Convert.ToDouble(p.LTV_plane_sky_prop_bridge_valley_boats_sand),
 								  LTV_plane_clouds_jet_sky_mountain_water_snow = Convert.ToDouble(p.LTV_plane_clouds_jet_sky_mountain_water_snow),
 								  LTV_snow_bear_polar_water_rocks_fox_sand = Convert.ToDouble(p.LTV_snow_bear_polar_water_rocks_fox_sand),
 								  LTV_sky_water_people_tree_sand_swimmers_clouds = Convert.ToDouble(p.LTV_sky_water_people_tree_sand_swimmers_clouds),
 								  Tag_reefs = (p.Tag_reefs=="True"),
 								  Tag_birds = (p.Tag_birds=="True"),
 								  Tag_ground = (p.Tag_ground=="True"),
 								  Tag_hills = (p.Tag_hills=="True"),
 								  Tag_rose = (p.Tag_rose=="True"),
 								  Tag_sky = (p.Tag_sky=="True"),
 								  Tag_window = (p.Tag_window=="True"),
 								  Tag_town = (p.Tag_town=="True"),
 								  Tag_woman = (p.Tag_woman=="True"),
 								  Tag_garden = (p.Tag_garden=="True"),
 								  Tag_bear = (p.Tag_bear=="True"),
 								  Tag_coast = (p.Tag_coast=="True"),
 								  Tag_railroad = (p.Tag_railroad=="True"),
 								  Tag_clouds = (p.Tag_clouds=="True"),
 								  Tag_harbor = (p.Tag_harbor=="True"),
 								  Tag_pillar = (p.Tag_pillar=="True"),
 								  Tag_white__tailed = (p.Tag_white__tailed=="True"),
 								  Tag_rocks = (p.Tag_rocks=="True"),
 								  Tag_sand = (p.Tag_sand=="True"),
 								  Tag_man = (p.Tag_man=="True"),
 								  Tag_night = (p.Tag_night=="True"),
 								  Tag_tower = (p.Tag_tower=="True"),
 								  Tag_river = (p.Tag_river=="True"),
 								  Tag_ruins = (p.Tag_ruins=="True"),
 								  Tag_grizzly = (p.Tag_grizzly=="True"),
 								  Tag_people = (p.Tag_people=="True"),
 								  Tag_house = (p.Tag_house=="True"),
 								  Tag_village = (p.Tag_village=="True"),
 								  Tag_sign = (p.Tag_sign=="True"),
 								  Tag_street = (p.Tag_street=="True"),
 								  Tag_palm = (p.Tag_palm=="True"),
 								  Tag_zebra = (p.Tag_zebra=="True"),
 								  Tag_sea = (p.Tag_sea=="True"),
 								  Tag_foals = (p.Tag_foals=="True"),
 								  Tag_leaf = (p.Tag_leaf=="True"),
 								  Tag_dunes = (p.Tag_dunes=="True"),
 								  Tag_sun = (p.Tag_sun=="True"),
 								  Tag_fox = (p.Tag_fox=="True"),
 								  Tag_skyline = (p.Tag_skyline=="True"),
 								  Tag_ice = (p.Tag_ice=="True"),
 								  Tag_prop = (p.Tag_prop=="True"),
 								  Tag_indian = (p.Tag_indian=="True"),
 								  Tag_landscape = (p.Tag_landscape=="True"),
 								  Tag_formula = (p.Tag_formula=="True"),
 								  Tag_temple = (p.Tag_temple=="True"),
 								  Tag_mare = (p.Tag_mare=="True"),
 								  Tag_roofs = (p.Tag_roofs=="True"),
 								  Tag_cars = (p.Tag_cars=="True"),
 								  Tag_bulls = (p.Tag_bulls=="True"),
 								  Tag_water = (p.Tag_water=="True"),
 								  Tag_tracks = (p.Tag_tracks=="True"),
 								  Tag_stone = (p.Tag_stone=="True"),
 								  Tag_island = (p.Tag_island=="True"),
 								  Tag_coral = (p.Tag_coral=="True"),
 								  Tag_locomotive = (p.Tag_locomotive=="True"),
 								  Tag_turn = (p.Tag_turn=="True"),
 								  Tag_horizon = (p.Tag_horizon=="True"),
 								  Tag_castle = (p.Tag_castle=="True"),
 								  Tag_road = (p.Tag_road=="True"),
 								  Tag_wall = (p.Tag_wall=="True"),
 								  Tag_canyon = (p.Tag_canyon=="True"),
 								  Tag_plants = (p.Tag_plants=="True"),
 								  Tag_church = (p.Tag_church=="True"),
 								  Tag_swimmers = (p.Tag_swimmers=="True"),
 								  Tag_market = (p.Tag_market=="True"),
 								  Tag_city = (p.Tag_city=="True"),
 								  Tag_jet = (p.Tag_jet=="True"),
 								  Tag_tusks = (p.Tag_tusks=="True"),
 								  Tag_valley = (p.Tag_valley=="True"),
 								  Tag_athlete = (p.Tag_athlete=="True"),
 								  Tag_horses = (p.Tag_horses=="True"),
 								  Tag_flight = (p.Tag_flight=="True"),
 								  Tag_frost = (p.Tag_frost=="True"),
 								  Tag_park = (p.Tag_park=="True"),
 								  Tag_lawn = (p.Tag_lawn=="True"),
 								  Tag_tundra = (p.Tag_tundra=="True"),
 								  Tag_hut = (p.Tag_hut=="True"),
 								  Tag_train = (p.Tag_train=="True"),
 								  Tag_flowers = (p.Tag_flowers=="True"),
 								  Tag_steel = (p.Tag_steel=="True"),
 								  Tag_frozen = (p.Tag_frozen=="True"),
 								  Tag_runway = (p.Tag_runway=="True"),
 								  Tag_tree = (p.Tag_tree=="True"),
 								  Tag_cat = (p.Tag_cat=="True"),
 								  Tag_shops = (p.Tag_shops=="True"),
 								  Tag_grass = (p.Tag_grass=="True"),
 								  Tag_sculpture = (p.Tag_sculpture=="True"),
 								  Tag_display = (p.Tag_display=="True"),
 								  Tag_bridge = (p.Tag_bridge=="True"),
 								  Tag_palace = (p.Tag_palace=="True"),
 								  Tag_door = (p.Tag_door=="True"),
 								  Tag_mountain = (p.Tag_mountain=="True"),
 								  Tag_scotland = (p.Tag_scotland=="True"),
 								  Tag_snow = (p.Tag_snow=="True"),
 								  Tag_field = (p.Tag_field=="True"),
 								  Tag_forest = (p.Tag_forest=="True"),
 								  Tag_branch = (p.Tag_branch=="True"),
 								  Tag_boats = (p.Tag_boats=="True"),
 								  Tag_beach = (p.Tag_beach=="True"),
 								  Tag_polar = (p.Tag_polar=="True"),
 								  Tag_buildings = (p.Tag_buildings=="True"),
 								  Tag_hotel = (p.Tag_hotel=="True"),
 								  Tag_nest = (p.Tag_nest=="True"),
 								  Tag_petals = (p.Tag_petals=="True"),
 								  Tag_plane = (p.Tag_plane=="True"),
 								  Tag_statue = (p.Tag_statue=="True"),
 								  Tag_waves = (p.Tag_waves=="True"),
 								  Tag_arch = (p.Tag_arch=="True"),
 								  Tag_desert = (p.Tag_desert=="True"),
 								  Tag_pool = (p.Tag_pool=="True"),
 								  Tag_cliff = (p.Tag_cliff=="True"),
 								  Tag_tiger = (p.Tag_tiger=="True"),
 								  Tag_close__up = (p.Tag_close__up=="True"),
 								  Tag_reflection = (p.Tag_reflection=="True"),
 								  Tag_ocean = (p.Tag_ocean=="True"),
 								  Tag_tulip = (p.Tag_tulip=="True"),
 								  Tag_shore = (p.Tag_shore=="True"),
 								  Tag_sunset = (p.Tag_sunset=="True"), 
 							 }; 
 							 context.AddToResources(img); 
 							 string[] imagesInFolder = Directory.GetFiles(imgPath, p.ImageID + ".*"); 
 							 // Create a Zentity file. 
 							 FileInfo ImageFile = new FileInfo(imagesInFolder[0]); 
 							 Zentity.Core.File fileResource = new Zentity.Core.File(); 
 							 fileResource.Title = ImageFile.Name; 
 							 fileResource.Size = ImageFile.Length; 
 							 fileResource.DateAdded = ImageFile.CreationTime; 
 							 fileResource.DateModified = ImageFile.LastWriteTime; 
 							 fileResource.FileExtension = ImageFile.Extension; 
 							 fileResource.MimeType = "image/" + fileResource.FileExtension.Replace(".", string.Empty); 
 							 // Add the file to context.     
 							 context.AddToResources(fileResource); 
 							 Console.WriteLine("[INFO] Creating image {0}", p.ImageID); 
 							 context.SaveChanges(); 
 							 // Now upload the actual binary content of the file.     
 							 FileStream fStream = new FileStream(ImageFile.FullName, FileMode.Open, FileAccess.Read); 
 							 Console.WriteLine("[INFO] Saving image {0} file", p.ImageID); 
 							 context.UploadFileContent(fileResource, fStream); 
 							 //Asociate file with Resource 
 							 img.Files.Add(fileResource); 
 							 context.InsertResourceHasFile(fileResource.Id, img.Id); 
 							 //Save Changes in context 
 							 Console.WriteLine("[INFO] Associating image {0} and file", p.ImageID); 
 							 context.SaveChanges(); 
 							 } 
 							 catch{ 
 								 Console.WriteLine("[ERROR] During image {0} creation", p.ImageID); 
 								 continue; 
 							 } 
 						 } 
 				 } 
 			 } 
 		 static void Main(string[] args) 
 		 { 
 			 const string connectionString = @"provider=System.Data.SqlClient; 
 				 metadata=../data/code/code/Zentity.Corel52.ExtendedCore.csdl|../data/code/code/Zentity.Corel52.csdl|../data/code/code/Zentity.Corel52.Consolidated.msl|../data/code/code/Zentity.Corel52.Consolidated.ssdl; 
 				 provider connection string='Data Source=.; 
 				 Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True' 
 				 "; 
 			 DataInsert dataUploader = new DataInsert(); 
 			 string imgFolderPath = "../data/images/"; 
 			 string ZXMLPath = "../data/ZXML/"; 
 			 string[] ZXMLFiles = Directory.GetFiles(ZXMLPath, "Images*.*"); 
 			 foreach (string a in ZXMLFiles) 
 			 { 
 				 ZentityContext zenContext = new ZentityContext(connectionString); 
 				 dataUploader.insertData_Corel5Image2(zenContext, a, imgFolderPath); 
 			 }
		 }
	 }
 }