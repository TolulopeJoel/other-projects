import api, { apiWithoutToken } from "../api";
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Link from '@mui/material/Link';
import React, { useState } from "react";
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import { useNavigate } from "react-router-dom";
import TextField from '@mui/material/TextField';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import CssBaseline from '@mui/material/CssBaseline';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { createTheme, ThemeProvider } from '@mui/material/styles';


function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'© Pass Store'} {new Date().getFullYear()}
    </Typography>
  );
}

const theme = createTheme();

function SignIn() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await apiWithoutToken.post("http://localhost:8000/api/auth/login/", {
        username,
        password,
      });
      const token = response.data.access;
      api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      localStorage.setItem('access_token', token)
      navigate("/");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField margin="normal" required fullWidth label="Username" name="text" autoFocus value={username} onChange={(event) => setUsername(event.target.value)} />
            <TextField margin="normal" required fullWidth label="Password" type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
            <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} > Sign In </Button>
            <Grid container>
              <Grid item xs>
                {/* <Link href="#" variant="body2"> Forgot password? </Link> */}
              </Grid>
              <Grid item>
                <Link href="/sign-up" variant="body2"> {"Don't have an account? Sign Up"} </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
}

export default SignIn;